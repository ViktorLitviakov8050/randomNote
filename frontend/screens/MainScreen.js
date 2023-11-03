import { View, StyleSheet, Alert } from 'react-native'
import React, { useEffect, useState } from 'react'
import Button from '../components/Button'
import Note from '../components/Note'
import useNotificationNote from '../hooks/useNotificationNote';
import useAPI from '../hooks/useAPI';

const MainScreen = () => {
    const [note, setNote] = useState({})
    const [stackNotes, setStackNotes] = useState([])

    const { fetchData: fetchRandomNote } = useAPI(`notes/getrandomnote`, setNote, console.log);
    const { fetchData: fetchPreviousNote } = useAPI(`notes/${stackNotes[stackNotes.length - 1]}`, setNote, console.log);
    

    useNotificationNote(setNote)
    const getNextNote = () => {
        setStackNotes((stackNotes) => [...stackNotes, note.id])
        fetchRandomNote();
    }
    
    const getPreviousNote = () => {
        stackNotes.pop()
        fetchPreviousNote();
    }

    useEffect(() => {
        fetchRandomNote();
    }, []);

    const isNotePresent = JSON.stringify(note) !== '{}'
    const isPreviousNotePresent = stackNotes.filter(Number).length > 0;

    return (
        <View style={styles.container}>
            {isNotePresent && <Note data={note} />}
            <View style={styles.buttons_container}>
                <Button color='orange' title="Previous" onPress={getPreviousNote} disabled={!isPreviousNotePresent} />
                <Button color='green' title="Next" onPress={getNextNote} />
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
    buttons_container: {
        flexDirection: 'row',
        paddingBottom: 10,
        width: '100%'
    },

})

export default MainScreen;
