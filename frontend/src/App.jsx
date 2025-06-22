import { useState, useEffect, useRef } from 'react';
import Header from './components/Header';
import MessageList from './components/MessageList';
import InputForm from './components/InputForm';

function App() {
  const [driveFolderId, setDriveFolderId] = useState('');
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    setMessages([
      { sender: 'ai', text: 'Hello! I am the Heritage Square AI assistant. How can I help you today?' }
    ]);
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim() || isLoading || !driveFolderId.trim()) return;

    const userMessage = { sender: 'user', text: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      // Use the environment variable for the API URL
      const apiUrl = `${import.meta.env.VITE_API_BASE_URL}/api/v1/qa/ask`;

      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          drive_folder_id: driveFolderId,
          question: input,
        }),
      });

      if (!response.ok) throw new Error(`API Error: ${response.statusText}`);
      const data = await response.json();
      const aiMessage = { sender: 'ai', text: data.answer };
      setMessages(prev => [...prev, aiMessage]);

    } catch (error) {
      console.error("Failed to get answer:", error);
      const errorMessage = { sender: 'ai', text: "Sorry, I encountered an error. Please try again." };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-heritage-green font-sans">
      <Header
        driveFolderId={driveFolderId}
        setDriveFolderId={setDriveFolderId}
      />
      <MessageList
        messages={messages}
        isLoading={isLoading}
        messagesEndRef={messagesEndRef}
      />
      <InputForm
        input={input}
        setInput={setInput}
        handleSubmit={handleSubmit}
        isLoading={isLoading}
        isChatDisabled={!driveFolderId.trim()}
      />
    </div>
  );
}

export default App;
