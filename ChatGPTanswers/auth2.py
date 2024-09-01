'''
OAuth 2.0 is a framework that allows apps to securely access your information on other websites without
needing to know your password. Instead of giving your password to an app, you give permission for that app to
 get a "key" (called a token) that grants limited access to your account.

### How It Works:

1. **User Permission**: You, the user, are asked to grant permission for an app to access your information.
This might happen, for example, when an app asks if it can access your Facebook account to log you in.

2. **Access Token**: If you agree, the app gets an "access token" from the service you're using (like Facebook or Google).
This token acts like a temporary key that lets the app access specific information (like your email address) without knowing your password.

3. **Limited Access**: The token only allows access to what you agreed to share. The app can't access other information or
 perform actions outside of the permissions you've given.

4. **Expiration**: The token often expires after a certain period, or you can revoke it whenever you want,
cutting off the app's access.

### Why It's Useful:

- **Security**: You don’t have to give out your password, reducing the risk if the app is compromised.
- **Control**: You can control what information the app can access and can revoke access whenever you choose.

### Example:

Imagine you’re using a travel app that wants to import your contacts from Google to help you plan a trip.
Instead of giving the app your Google password, you authorize it to access your contacts through OAuth 2.0.
The app then gets a token, retrieves your contacts, and can’t do anything else with your Google account.

In simple terms, OAuth 2.0 is like giving someone a guest pass to your house that only lets them into the
living room and expires after a day. They don’t get the keys to the whole house, and you can take back the pass
whenever you want.


'''
