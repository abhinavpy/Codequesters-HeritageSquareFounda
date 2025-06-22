import React, { useEffect, useRef } from 'react';
import Message from './Message';
import { SparklesIcon } from '@heroicons/react/24/solid';

const MessageList = ({ messages, isLoading, messagesEndRef }) => {
  const containerRef = useRef(null);

  // Smooth scroll animation
  useEffect(() => {
    if (containerRef.current) {
      containerRef.current.scrollTo({
        top: containerRef.current.scrollHeight,
        behavior: 'smooth'
      });
    }
  }, [messages, isLoading]);

  return (
    <main 
      ref={containerRef}
      className="flex-1 overflow-y-auto px-4 py-6 bg-gradient-to-b from-heritage-green to-heritage-green/95"
      style={{
        backgroundImage: `radial-gradient(circle at 20% 50%, rgba(212, 175, 55, 0.1) 0%, transparent 50%),
                         radial-gradient(circle at 80% 20%, rgba(212, 175, 55, 0.05) 0%, transparent 50%),
                         radial-gradient(circle at 40% 80%, rgba(212, 175, 55, 0.05) 0%, transparent 50%)`
      }}
    >
      <div className="max-w-4xl mx-auto space-y-1">
        {messages.map((msg, index) => (
          <div
            key={index}
            className="animate-fadeIn"
            style={{ animationDelay: `${index * 100}ms` }}
          >
            <Message sender={msg.sender} text={msg.text} />
          </div>
        ))}
        
        {/* Enhanced Loading State */}
        {isLoading && (
          <div className="animate-fadeIn">
            <Message sender="ai" text="" isTyping={true} />
          </div>
        )}
        
        <div ref={messagesEndRef} />
      </div>
    </main>
  );
};

export default MessageList;