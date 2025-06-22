import React from 'react';

const Header = ({ driveFolderId, setDriveFolderId }) => {
  return (
    <header className="p-4 border-b border-heritage-off-white/20 text-center space-y-4">
      <h1 className="font-serif text-3xl text-heritage-off-white">Heritage Square AI Assistant</h1>
      <div className="max-w-md mx-auto">
        <input
          type="text"
          value={driveFolderId}
          onChange={(e) => setDriveFolderId(e.target.value)}
          placeholder="Enter Google Drive Folder ID here..."
          className="w-full p-2 bg-heritage-off-white/20 text-heritage-off-white placeholder:text-heritage-off-white/60 rounded-md focus:outline-none focus:ring-2 focus:ring-heritage-gold text-center"
        />
      </div>
    </header>
  );
};

export default Header;