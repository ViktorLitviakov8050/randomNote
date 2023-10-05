import { StyleSheet, View, Text, SafeAreaView } from 'react-native';
import AuthScreen from './screens/AuthScreen';
import MainScreen from './screens/MainScreen';
import { StatusBar } from 'expo-status-bar';
import registerNNPushToken from 'native-notify';


export default function App() {
  registerNNPushToken(13004, 'mtizi9JKDcsxzzbsbpXdeY');
  return (
    <SafeAreaView style={styles.app}>
      <View style={styles.container}>
        <Text style={styles.header}>---</Text>
        {/* <AuthScreen /> */}
        <MainScreen />
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  app: {
    flex: 1,
    backgroundColor: 'aquamarine',
    alignItems: 'center',
    justifyContent: 'center',
  },
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 30
  },
  header: {
    fontSize: 56
  }
});


