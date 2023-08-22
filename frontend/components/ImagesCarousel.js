import Carousel from 'react-native-reanimated-carousel';
import {View, Dimensions} from 'react-native'


function ImagesCarousel({ data }) {
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

export default ImagesCarousel