import { Text, Pressable } from 'react-native'
import React from 'react'

const Button = (props) => {
    return (
        <Pressable
            disabled={props.disabled}
            onPress={props.onPress}
            style={[styles.button, { backgroundColor: props?.color, opacity:props.disabled ? 0.5 :1 }]}
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