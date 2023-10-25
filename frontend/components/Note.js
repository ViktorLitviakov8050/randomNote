import { View, Text, Image, StyleSheet, ScrollView } from 'react-native'
import React, { useEffect, useState } from 'react'
import ImagesCarousel from './ImagesCarousel'


const getImages = async (callback, id) => {
    try {
        const response = await fetch(
            `http://192.168.1.91:8000/notes/getimages/${id}`,
        );
        const json = await response.json();
        callback(json.images);
    } catch (error) {
        console.error(error);
    }
};


const Note = ({ data: note }) => {

    const [images, setImages] = useState([])

    useEffect(() => {
            getImages(setImages, note.id)
    }, []);


    const imagesList = images?.map((image) => {
        return (
            <Image
                key={image}
                style={{ height: 300, width: 500 }}
                source={{ uri: `data:image/png;base64,${image}` }}
                resizeMode='center'
            />
        )
    })
    const labels = note.labels?.map((label) => {
        return (
            <Text
                key={label.name}
            >{label.name}</Text>
        )
    })

    return (
        <ScrollView contentContainerStyle={styles.scrollable_container}>
            <Text style={styles.noteTitle}>{note.title}</Text>
            <Text style={styles.noteText}>{note.text_content}</Text>
            <View style={styles.labels_container}>
                {labels?.map(label => label)}
            </View>
            <ImagesCarousel data={imagesList} />
        </ScrollView>
    )
}

const styles = StyleSheet.create({
    scrollable_container: {
        marginBottom: 30
    },
    noteTitle: {
        fontSize: 36,
        textAlign: 'center',
        padding: 20,

    },
    noteText: {
        textAlign: 'center',
        padding: 20,
        fontSize: 20
    },
    labels_container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'space-between'
    }
})

export default Note