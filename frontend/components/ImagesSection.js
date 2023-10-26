import { View, Image } from 'react-native'
import React, { useEffect, useState } from 'react'
import ImagesCarousel from './ImagesCarousel'
import useAPI from '../hooks/useAPI'

export default function ImagesSection({ note_id }) {
    const [images, setImages] = useState([]);
    const { loading, fetchData } = useAPI(`notes/getimages/${note_id}`, ({ images }) => setImages(images), console.log);

    useEffect(() => {
        fetchData();
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
