import spotipy
import spotipy.util as util
import yaml

stream = open('config.yaml')
user_config = yaml.load(stream, Loader=yaml.FullLoader)
token = util.prompt_for_user_token('0aawyoae0w7swyq8m3op5276n', 
        scope='playlist-read-private', 
        client_id='e9f8bbbe8e044a4f9db3516ebea16dd1', 
        client_secret='4c267f7c2fe64054a2cbe2ee868f03c5', 
        redirect_uri='http://localhost:9000/')
print(token)
spotipy.Spotify(auth=token)
