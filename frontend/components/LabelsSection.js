import { View, Text, StyleSheet } from 'react-native'
import React from 'react'

export default function LabelsSection({ note_labels: labels }) {
    return (
        <View style={styles.labels_container}>
            {labels?.map(label => <Text
                key={label.name}
                style={styles.label}
            >{label.name}</Text>)}
        </View>
    )
}

const styles = StyleSheet.create({
    labels_container: {
        flex: 1,
        marginHorizontal: 30,
        alignItems: 'center',
        justifyContent: 'space-between',
    },
    label: {
        fontSize: 18,
        color: 'red'
    }
})
