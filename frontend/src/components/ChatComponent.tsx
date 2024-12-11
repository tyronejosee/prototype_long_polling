import React from 'react';
import useChatUpdates from '../hooks/useChatUpdates';
import { Message } from '../interfaces/message.interface';


const ChatComponent: React.FC = () => {
    const { messages, loading } = useChatUpdates('http://localhost:8000/api/chat-updates/');

    return (
        <div>
            <h1>Chat</h1>
            {loading && <p>Loading...</p>}
            <ul>
                {messages.map((message: Message) => (
                    <li key={message.id}>
                        {message.content} -{' '}
                        {new Date(message.timestamp * 1000).toLocaleTimeString()}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ChatComponent;
