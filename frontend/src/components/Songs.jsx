import React, { useEffect, useState } from 'react';
import api from "../api.js";
import AddSongForm from './AddSongForm';

const SongList = () => {
  const [fruits, setSongs] = useState([]);

  const fetchSongs = async () => {
    try {
      const response = await api.get('/songs');
      setSongs(response.data.songs);
    } catch (error) {
      console.error("Error fetching songs", error);
    }
  };

  const addSong = async (songName) => {
    try {
      await api.post('/songs', { name: songName });
      fetchSongs();  // Refresh the list after adding a fruit
    } catch (error) {
      console.error("Error adding song", error);
    }
  };

  useEffect(() => {
    fetchSongs();
  }, []);

  return (
    <div>
      <h2>Songs List</h2>
      <ul>
        {songs.map((song, index) => (
          <li key={index}>{song.name}</li>
        ))}
      </ul>
      <AddSongForm addSong={addSong} />
    </div>
  );
};

export default SongList;