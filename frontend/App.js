import MainScreen from './screens/MainScreen';
import { Text, View, StyleSheet, SafeAreaView } from 'react-native';

export default function App() {
  return (
    <SafeAreaView style={styles.app}>
      <View style={styles.container}>
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


