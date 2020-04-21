import logging
import pickle
from pathlib import Path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


from googleapiclient.http import MediaIoBaseDownload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata',
          'https://www.googleapis.com/auth/drive.photos.readonly',
          'https://www.googleapis.com/auth/drive']

logger = logging.getLogger(__name__)


class GoogleService:
    def __init__(self, credentials_path='credentials.json'):
        """
        Will store a google resources object with methods for interacting with the service.

        Args:
            credentials_path (string): Path to the credentials file generated on google console
        """
        self.scopes = SCOPES
        self.service = None
        self._init_service(credentials_path)

    def _init_service(self, credentials_path):
        """ Prompts the user to allow access to the app for all the scopes selected """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if Path('token.pickle').exists():
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('drive', 'v3', credentials=creds)

    def download_image(self, name='image', path=''):
        """
        Fetch files from the service and saves the first image found on a <name>.png file

        Args:
            name (string): name of the file where the image will be stored
            path (string): destination path where the image will be saved
        """
        results = self.service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            logger.error('No files found.')
            return False

        for image in [item for item in items if item['name'].endswith('.jpg')]:
            logger.debug(f'Image {image["name"]} found')
            request = self.service.files().get_media(fileId=image['id'])
            with open(Path(path, f'{name}.png'), 'wb') as image_file:
                downloader = MediaIoBaseDownload(image_file, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    logger.info("Download %d%%." % int(status.progress() * 100))
                logger.info(f'Image {image["name"]} successfully downloaded')
                break
