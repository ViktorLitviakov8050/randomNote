import { Text, Pressable } from 'react-native'
import React from 'react'

const Button = (props) => {
    return (
        <Pressable
            onPress={props.onPress}
            style={[styles.button, { backgroundColor: props?.color }]}
        >
            <Text style={styles.buttonText}>
                {props?.title}
            </Text>
        </Pressable>
    )
}

export default Button

const styles = {
    button: {
        flex: 1,
        paddingVertical: 10,
        borderRadius: 30
    },
    buttonText: {
        color: 'white',
        textAlign: 'center',
        textAlignVertical: 'center',
        fontSize: 28,
    }
}