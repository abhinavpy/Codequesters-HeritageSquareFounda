import React from 'react';
import { PaperAirplaneIcon } from '@heroicons/react/24/solid';

const Header = () => {
  return (
    <header className="p-4 border-b border-heritage-off-white/20 text-center">
      <h1 className="font-serif text-3xl text-heritage-off-white">Heritage Square AI Assistant</h1>
    </header>
  );
};

const InputForm = ({ input, setInput, handleSubmit, isLoading, isChatDisabled }) => {
  return (
    <footer className="p-4 border-t border-heritage-off-white/20">
      <form onSubmit={handleSubmit} className="flex items-center gap-4 max-w-3xl mx-auto">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder={isChatDisabled ? "Please enter a Folder ID above to begin" : "Ask a question about Heritage Square..."}
          className="flex-1 p-3 bg-heritage-off-white/90 text-heritage-green placeholder:text-heritage-green/60 rounded-md focus:outline-none focus:ring-2 focus:ring-heritage-gold"
          disabled={isLoading || isChatDisabled}
        />
        <button
          type="submit"
          className="p-3 bg-heritage-off-white text-heritage-green rounded-md disabled:opacity-50 hover:bg-white transition-colors focus:outline-none focus:ring-2 focus:ring-heritage-gold"
          disabled={isLoading || isChatDisabled}
        >
          <PaperAirplaneIcon className="w-6 h-6" />
        </button>
      </form>
    </footer>
  );
};

export default InputForm;