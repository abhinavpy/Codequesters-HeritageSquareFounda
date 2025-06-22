import React from 'react';

const Header = ({ driveFolderId, setDriveFolderId }) => {
  return (
    <header className="relative backdrop-blur-md bg-heritage-green/80 border-b border-heritage-off-white/10 shadow-lg">
      {/* Background Pattern */}
      <div className="absolute inset-0 bg-gradient-to-r from-heritage-green/50 to-heritage-green/30"></div>
      
      <div className="relative p-6 text-center space-y-4">
        {/* Title with Enhanced Typography */}
        <div className="space-y-2">
          <h1 className="font-serif text-4xl sm:text-5xl text-heritage-off-white font-bold tracking-wide">
            Heritage Square
          </h1>
          <p className="text-heritage-off-white/80 text-lg font-light tracking-wider">
            AI Assistant
          </p>
        </div>

        {/* Enhanced Folder ID Input */}
        <div className="max-w-md mx-auto">
          <div className="relative group">
            <input
              type="text"
              value={driveFolderId}
              onChange={(e) => setDriveFolderId(e.target.value)}
              placeholder="Enter Google Drive Folder ID..."
              className="
                w-full p-4 bg-heritage-off-white/10 backdrop-blur-sm
                text-heritage-off-white placeholder:text-heritage-off-white/50
                border border-heritage-off-white/20 rounded-xl
                focus:outline-none focus:ring-2 focus:ring-heritage-gold/50 focus:border-heritage-gold/50
                transition-all duration-300 text-center font-medium
                group-hover:bg-heritage-off-white/15
              "
            />
            <div className="absolute inset-0 rounded-xl bg-gradient-to-r from-heritage-gold/0 via-heritage-gold/5 to-heritage-gold/0 opacity-0 group-focus-within:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;