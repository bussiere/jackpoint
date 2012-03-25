         my_crypt = CRYPT(key=auth.settings.hmac_key)
    crypt_pass = my_crypt(password)[0]    
    id_user = db.auth_user.insert(
                   Surnom=Surnom,
                   email=email,
                   Items = None,
                   Skills = None,
                   password=crypt_pass,
                                   )
        db.commit()
        session.auth = Storage(user=user,expiration=auth.settings.expiration,hmac_key=str(uuid4()))
        auth.login_bare(form.vars.email,form.vars.invitation)