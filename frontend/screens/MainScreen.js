import { View, Text, Image, Dimensions, Button, StyleSheet } from 'react-native'
import React from 'react'
import note from '../mocks/note'
import Carousel from 'react-native-reanimated-carousel';

const MainScreen = () => {
    const images = note.images.map((imageURL) => <Image
        key={imageURL}
        style={{ width: 500, height: 500 }}
        source={{ uri: imageURL }}
    />)
    return (
        <View style={styles.main_container}>
            <Text>{note.text}</Text>
            <Index data={images} />
            <View style={styles.container}>
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
    container: {
        flexDirection: 'row',
        justifyContent: 'space-between', // Create space between buttons
        paddingHorizontal: 20, // Add horizontal padding
        marginTop: 10 ,// Add top margin
        height: Dimensions.get('window').width / 2, // Set a specific height
    },
})

export default MainScreen

function Index({ data }) {
    const width = Dimensions.get('window').width;
    return (
        <View style={{ flex: 1 }}>
            <Carousel
                loop
                width={width}
                height={width / 2}
                autoPlay={true}
                data={data}
                scrollAnimationDuration={1000}
                onSnapToItem={(index) => console.log('current index:', index)}
                renderItem={({ item }) => (
                    <View
                        style={{
                            flex: 1,
                            justifyContent: 'center',
                            alignItems: 'center'
                        }}
                    >
                        {item}

                    </View>
                )}
            />
        </View>
    );
}

