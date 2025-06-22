import React from 'react';
import { UserIcon, SparklesIcon } from '@heroicons/react/24/solid';

const Message = ({ sender, text, isTyping = false }) => {
  const isUser = sender === 'user';

  return (
    <div className={`flex items-end gap-3 mb-6 ${isUser ? 'justify-end' : 'justify-start'}`}>
      {/* AI Avatar */}
      {!isUser && (
        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-heritage-gold/20 to-heritage-green/30 flex items-center justify-center shadow-lg border border-heritage-gold/30">
          <SparklesIcon className="w-4 h-4 text-heritage-gold" />
        </div>
      )}

      {/* Message Bubble */}
      <div 
        className={`
          group relative max-w-xs sm:max-w-md lg:max-w-lg xl:max-w-xl 
          ${isUser 
            ? 'bg-gradient-to-br from-heritage-off-white to-heritage-off-white/90 text-heritage-green shadow-lg' 
            : 'bg-gradient-to-br from-heritage-green/40 to-heritage-green/60 text-heritage-off-white shadow-md border border-heritage-off-white/10'
          }
          rounded-2xl px-4 py-3 backdrop-blur-sm
          ${isUser ? 'rounded-br-md ml-12' : 'rounded-bl-md mr-12'}
          transform transition-all duration-200 hover:scale-[1.02]
        `}
      >
        {/* Message Text */}
        <div className={`text-sm leading-relaxed ${isUser ? 'text-heritage-green' : 'text-heritage-off-white/95'}`}>
          {isTyping ? (
            <TypingIndicator />
          ) : (
            <p className="whitespace-pre-wrap break-words font-medium">
              {text}
            </p>
          )}
        </div>

        {/* Message Tail */}
        <div 
          className={`
            absolute w-3 h-3 transform rotate-45
            ${isUser 
              ? 'bg-gradient-to-br from-heritage-off-white to-heritage-off-white/90 -bottom-1 -right-1' 
              : 'bg-gradient-to-br from-heritage-green/40 to-heritage-green/60 -bottom-1 -left-1'
            }
          `}
        />
      </div>

      {/* User Avatar */}
      {isUser && (
        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-heritage-off-white/90 to-heritage-off-white flex items-center justify-center shadow-lg">
          <UserIcon className="w-4 h-4 text-heritage-green" />
        </div>
      )}
    </div>
  );
};

// Enhanced Typing Indicator Component
const TypingIndicator = () => {
  return (
    <div className="flex items-center space-x-1 py-1">
      <div className="flex space-x-1">
        <div className="w-2 h-2 bg-heritage-off-white/70 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
        <div className="w-2 h-2 bg-heritage-off-white/70 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
        <div className="w-2 h-2 bg-heritage-off-white/70 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
      </div>
      <span className="text-heritage-off-white/70 text-xs ml-2">AI is thinking...</span>
    </div>
  );
};

export default Message;