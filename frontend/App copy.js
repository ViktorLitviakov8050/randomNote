import { useEffect, useState } from "react";
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button } from 'react-native';
import * as WebBrowser from "expo-web-browser";
import * as Google from "expo-auth-session/providers/google";

const ClientID = "385761316947-5bp3dhevk2gk3cheoteb0ehfa9kp0cq5.apps.googleusercontent.com"


WebBrowser.maybeCompleteAuthSession();


export default function App() {
  // const [token, setToken] = useState("");
  
  const [request, response, promptAsync] = Google.useAuthRequest({
    // androidClientId: "",
    // iosClientId: "",
    webClientId: ClientID,
  });

  useEffect(() => {
    if (response) console.log(response.authentication.accessToken);
  }, [response]);

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Random note for today!</Text>
      <Button title='Sign in' style={styles.button} onPress={() => promptAsync()}></Button>
      <StatusBar style="auto" />
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
  text: {color: "blue",
         fontSize: 50,
},
  button: {
    width: 30,
    height: 30,
}
});


