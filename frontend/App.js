import { StyleSheet, View } from 'react-native';
import AuthScreensss from './screens/AuthScreen';
import MainScreen from './screens/MainScreen';


export default function App() {

  return (
    <View style={styles.container}>
      {/* <AuthScreensss /> */}
      <MainScreen />

    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'aquamarine',
    alignItems: 'center',
    justifyContent: 'center',
  },
});


