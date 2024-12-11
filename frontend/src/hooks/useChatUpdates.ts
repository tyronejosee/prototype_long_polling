import { useState, useEffect } from 'react';
import { Message } from '../interfaces/message.interface';


const useChatUpdates = (url: string) => {
    const [messages, setMessages] = useState<Message[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [lastCheck, setLastCheck] = useState<number>(Date.now() / 1000);

    const fetchUpdates = async () => {
        try {
            const response = await fetch(`${url}?last_check=${lastCheck}`);
            if (response.status === 200) {
                const data = await response.json();
                setMessages((prevMessages) => [
                    ...prevMessages,
                    ...data.new_messages
                ]);
                setLastCheck(Date.now() / 1000);
            }
        } catch (error) {
            console.error('Error fetching chat updates:', error);
        } finally {
            setTimeout(fetchUpdates, 10000);
        }
    };

    useEffect(() => {
        fetchUpdates();
        setLoading(false);
        return () => setLoading(true);
    }, []);

    return { messages, loading };
};

export default useChatUpdates;
