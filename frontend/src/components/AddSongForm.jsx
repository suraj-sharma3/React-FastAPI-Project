import React, { useState } from 'react';

const AddSongForm = ({ addsong }) => {
  const [songName, setSongName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (songName) {
      addSong(songName);
      setSongName('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={songName}
        onChange={(e) => setSongName(e.target.value)}
        placeholder="Enter Song Name"
      />
      <button type="submit">Add Song</button>
    </form>
  );
};

export default AddSongForm;