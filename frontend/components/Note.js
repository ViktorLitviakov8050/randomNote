import LabelsSection from './LabelsSection';

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
                source={{ uri: image }}
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
            <LabelsSection note_labels={note.labels} />
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
