import React from 'react';
import { UserIcon, SparklesIcon } from '@heroicons/react/24/solid';

const Message = ({ sender, text }) => {
  const isUser = sender === 'user';

  return (
    <div className={`flex items-start gap-4 ${isUser ? 'justify-end' : ''}`}>
      {!isUser && (
        <div className="flex-shrink-0 w-10 h-10 rounded-full bg-heritage-off-white/10 flex items-center justify-center">
          <SparklesIcon className="w-6 h-6 text-heritage-gold" />
        </div>
      )}
      <div className={`max-w-xl p-4 rounded-lg ${isUser ? 'bg-heritage-off-white text-heritage-green' : 'bg-heritage-green/50'}`}>
        <p className="whitespace-pre-wrap">{text}</p>
      </div>
      {isUser && (
        <div className="flex-shrink-0 w-10 h-10 rounded-full bg-heritage-off-white/80 flex items-center justify-center">
          <UserIcon className="w-6 h-6 text-heritage-green" />
        </div>
      )}
    </div>
  );
};

export default Message;