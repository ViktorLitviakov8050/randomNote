import { View, Text, Image, Dimensions, StyleSheet, Pressable, ScrollView } from 'react-native'
import React, {useEffect, useState} from 'react'
import note from '../mocks/note'
import ImagesCarousel from '../components/ImagesCarousel'
import Button from '../components/Button'

const getRandomNote = async (callback) => {
    try {
        const response = await fetch(
            'http://192.168.1.91:8000/notes/getrandomnote',
            );
            const json = await response.json();
            callback(json);
        } catch (error) {
            console.error(error);
        }
    };

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

const MainScreen = () => {
    const [note, setNote] = useState({})
    const [images, setImages] = useState([])

    useEffect(() => {
            getRandomNote((json) => {
                setNote(json);
                getImages(setImages, json.id)})
        },[]);
    
    
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
        <View style={styles.container}>
            <ScrollView contentContainerStyle={styles.scrollable_container}>
                <Text style={styles.noteText}>{note.title}</Text>
                <Text style={styles.noteText}>{note.text_content}</Text>
                {labels?.map(label=>label)}
                <ImagesCarousel data={imagesList} />
            </ScrollView>
            <View style={styles.buttons_container}>
                <Button color='green' title="Next" onPress={() => getRandomNote(setNote)} />
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'space-between'
    },
    scrollable_container: {
        marginBottom: 30
    },
    noteText: {
        textAlign: 'center',
        padding: 20,
        fontSize: 20
    },
    buttons_container: {
        flexDirection: 'row',
        paddingBottom: 10,
        width: '100%'

    }
})

export default MainScreen


