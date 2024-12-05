import React from 'react';
import './App.css';
import SongList from './components/Songs';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Playlist App</h1>
      </header>
      <main>
        <SongList />
      </main>
    </div>
  );
};

export default App;