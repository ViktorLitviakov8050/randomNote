import { Text, StyleSheet, ScrollView } from 'react-native'
import React from 'react'
import ImagesSection from './ImagesSection';
import LabelsSection from './LabelsSection';

const Note = ({ data: note }) => {
    return (
        <ScrollView contentContainerStyle={styles.scrollable_container}>
            <Text style={styles.noteTitle}>{note.title}</Text>
            <Text style={styles.noteText}>{note.text_content}</Text>
            <LabelsSection note_labels={note.labels} />
            <ImagesSection note_id={note.id} />
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
    }
})

export default Note;
