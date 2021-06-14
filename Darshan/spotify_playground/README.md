# Setup
- To properly operate all files in this directory, make sure to create an application in your [Spotify Dashboard](https://developer.spotify.com/dashboard/).
  - Be sure to set the redirect URI in the settings of your new application to <https://example.com/callback/>
- Also make sure to set the following environment variables in your codespace before running any script in this directory, otherwise the oauth2 authentication will not work
  - SPOTIPY_CLIENT_ID (token found in spotify dashboard)
  - SPOTIPY_CLIENT_SECRET (token found in spotify dashboard)
  - SPOTIPY_REDIRECT_URI (defined earlier in dashboard settings. Make sure that the environment variable is exactly the same as it appears in the application settings in the dashboard)
