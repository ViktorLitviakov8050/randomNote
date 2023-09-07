import Carousel from 'react-native-reanimated-carousel';
import { View, Dimensions } from 'react-native'


function ImagesCarousel({ data }) {
    const { width, height } = Dimensions.get('window');

    return (
        <View style={{ flex: 1 }}>
            <Carousel
                loop
                width={width}
                height={height / 3}
                autoPlay={true}
                data={data}
                scrollAnimationDuration={1000}
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