import { View, Text, Image, Dimensions, Button, StyleSheet } from 'react-native'
import React from 'react'
import note from '../mocks/note'
import ImagesCarousel from '../components/ImagesCarousel'

const MainScreen = () => {
    const images = note.images.map((imageURL) => <Image
        key={imageURL}
        style={{ width: 500, height: 500 }}
        source={{ uri: imageURL }}
    />)
    return (
        <View style={styles.main_container}>
            <Text>{note.text}</Text>
            <ImagesCarousel data={images} />
            <View style={styles.button_container}>
                <Button title="Edit" onPress={alert}/>
                <Button title="Next" onPress={alert}/>
                <Button title="Delete" onPress={alert}/>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    main_container: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center',
      
    },
    button_container: {
        flexDirection: 'row',
        justifyContent: 'space-between', // Create space between buttons
        paddingHorizontal: 20, // Add horizontal padding
        marginTop: 10 ,// Add top margin
        height: Dimensions.get('window').width / 2, // Set a specific height
    },
})

export default MainScreen

