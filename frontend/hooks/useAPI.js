import { useState } from 'react';
import { API_URL } from "@env";

const useAPI = (endpoint, onSuccess, onError) => {
    const [loading, setLoading] = useState(false);

    const fetchData = async () => {
        try {
            setLoading(true);
            const response = await fetch(`${API_URL}/${endpoint}`);
            const json = await response.json();
            onSuccess(json);
            setLoading(false);
        } catch (error) {
            onError(error);
        }
    };

    return { loading, fetchData };
};

export default useAPI;
