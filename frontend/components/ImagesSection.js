import { View, Image } from 'react-native'
import React, { useEffect, useState } from 'react'
import ImagesCarousel from './ImagesCarousel'
import { API_URL } from "@env"



const getImages = async (callback, id) => {
    try {
        const response = await fetch(
            `${API_URL}/notes/getimages/${id}`,
        );
        const json = await response.json();
        callback(json.images);
    } catch (error) {
        console.error(error);
    }
};

export default function ImagesSection({ note_id }) {
    const [images, setImages] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        setLoading(true)
        getImages((images) => {
            setImages(images);
            setLoading(false);
        }, note_id)

    }, [note_id]);

    const imagesList = images?.map((image) => {
        return (
            <Image
                key={image}
                style={{ height: 300, width: 500 }}
                source={{ uri: image }}
                resizeMode='center'
            />
        )
    })
    const loadingBar = <View style={{
        flex: 1,
        alignItems: 'center',
    }}>
        <Image style={{ height: 150, width: 150 }} source={{ uri: "https://www.assamrifles.gov.in/onlineapp/images/processing.gif" }}></Image>
    </View>
    return (
        <>
            {loading ? loadingBar : <ImagesCarousel data={imagesList} />}
        </>
    )
}
