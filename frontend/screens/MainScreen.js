import { View, Text, Image, Dimensions, StyleSheet, Pressable, ScrollView } from 'react-native'
import React from 'react'
import note from '../mocks/note'
import ImagesCarousel from '../components/ImagesCarousel'
import Button from '../components/Button'

const MainScreen = () => {
    const images = note.images.map((imageURL) => {
        return (
            <Image
                key={imageURL}
                style={{ height: 300, width: 500 }}
                source={{ uri: imageURL }}
                resizeMode='center'
            />
        )
    })
    return (
        <View style={styles.container}>
            <ScrollView contentContainerStyle={styles.scrollable_container}>
                <Text style={styles.noteText}>{note.text}</Text>
                <ImagesCarousel data={images} />
            </ScrollView>
            <View style={styles.buttons_container}>
                <Button color='blue' title="Edit" onPress={() => alert('Edit')} />
                <Button color='green' title="Next" onPress={() => alert('Next')} />
                <Button color='red' title="Delete" onPress={() => alert('Delete')} />
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

    }
})

export default MainScreen


