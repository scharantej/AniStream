## Flask Application Design for Anime Streaming Website

### HTML Files

- **index.html**: Main page of the website, providing a search bar and a list of available anime.
- **anime.html**: Displays information about a specific anime, including its episodes.
- **episode.html**: Displays a specific episode of an anime.

### Routes

- **GET /**: Home page, displaying a search bar and list of anime.
- **GET /anime/:anime_id**: Displays information about a specific anime.
- **GET /anime/:anime_id/episode/:episode_id**: Displays a specific episode of an anime.
- **POST /search**: Search for anime based on title or genre.