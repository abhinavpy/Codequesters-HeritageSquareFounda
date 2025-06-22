import React from 'react';
import Message from './Message';
import { SparklesIcon } from '@heroicons/react/24/solid';

const MessageList = ({ messages, isLoading, messagesEndRef }) => {
  return (
    <main className="flex-1 overflow-y-auto p-6 space-y-6">
      {messages.map((msg, index) => (
        <Message key={index} sender={msg.sender} text={msg.text} />
      ))}
      {isLoading && (
        <div className="flex items-start gap-4">
          <div className="flex-shrink-0 w-10 h-10 rounded-full bg-heritage-off-white/10 flex items-center justify-center">
            <SparklesIcon className="w-6 h-6 text-heritage-gold animate-pulse" />
          </div>
          <div className="max-w-xl p-4 rounded-lg bg-heritage-green/50">
            <p>Thinking...</p>
          </div>
        </div>
      )}
      <div ref={messagesEndRef} />
    </main>
  );
};

export default MessageList;