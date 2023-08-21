import { useEffect, useState } from "react";
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';



export default function AuthScreen() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  function loginUser() {
    alert(`${email} ${password}`)
    }

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Random note for today!</Text>
      <TextInput value={email}
        placeholder="useless placeholder"
        onChangeText={setEmail}></TextInput>
      <TextInput value={password}
        placeholder="useless placeholder"
        onChangeText={setPassword}
        secureTextEntry></TextInput>

      <Button title='Sign in' style={styles.button} onPress={loginUser}></Button>
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
  text: {
    color: "blue",
    fontSize: 50,
  },
  button: {
    width: 30,
    height: 30,
  }
});


