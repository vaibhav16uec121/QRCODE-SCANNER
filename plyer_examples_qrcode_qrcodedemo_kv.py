#:kivy 1.8.0
<SingleMiddleTextInput@TextInput>:
    multiline: False
    padding_y: ( self.height - self.line_height ) / 2

<QRCodeDemo>:
    manager: manager
    BoxLayout:
        orientation: 'vertical'
        Label:
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint_y: 0.1
            text: 'QR Code Demo App'
            color: [0,0,0,1]
            bold: True
            font_size: sp(25)
        BoxLayout:
            padding: dp(20)
            size_hint_y: 0.7
            orientation: 'horizontal'
            AsyncImage:
                id: select_image
                allow_stretch: True
                source: root.file_location
            BoxLayout:
                orientation: 'vertical'
                spacing: dp(20)
                Spinner:
                    id: qr_type_select
                    text: "text"
                    values: root.qr_data_type
                    size_hint_y: 0.2
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_text: root.update_qr_type(self.text)
                ScreenManager:
                    id: manager
                    size_hint_y: 0.9
                    Screen:
                        name: 'text'
                        TextInput:
                            id: qr_text
                            hint_text: 'Text'
                    Screen:
                        name: 'url'
                        TextInput:
                            id: qr_url
                            multiline: False
                            hint_text: 'URL'
                    Screen:
                        name: 'email'
                        TextInput:
                            id: qr_email
                            multiline: False
                            hint_text: 'Email'
                    Screen:
                        name: 'emailmessage'
                        BoxLayout:
                            orientation: 'vertical'
                            spacing: dp(10)
                            TextInput:
                                id: qr_email_to
                                size_hint_y: 0.2
                                multiline: False
                                hint_text: 'To'
                            TextInput:
                                id: qr_email_sub
                                size_hint_y: 0.2
                                multiline: False
                                hint_text: 'Subject'
                            TextInput:
                                id: qr_email_body
                                size_hint_y: 0.8
                                hint_text: 'Body'
                    Screen:
                        name: 'bookmark'
                        BoxLayout:
                            orientation: 'vertical'
                            spacing: dp(10)
                            TextInput:
                                id: qr_bookmark_title
                                multiline: False
                                hint_text: 'Title'
                            TextInput:
                                id: qr_bookmark_url
                                multiline: False
                                hint_text: 'URL'
                    Screen:
                        name: 'geo'
                        BoxLayout:
                            orientation: 'vertical'
                            spacing: dp(10)
                            TextInput:
                                id: qr_get_lat
                                multiline: False
                                hint_text: 'Latitude'
                            TextInput:
                                id: qr_get_lon
                                multiline: False
                                hint_text: 'Longitude'
        GridLayout:
            size_hint_y: 0.3
            cols:2
            orientation: 'horizontal'
            spacing: dp(10)
            padding: dp(20)

            Button:
                text: 'Select Image'
                on_press: root.open_filepopup()
            Button:
                text: 'Scan (Camera)'
                on_press: root.open_webcam()
            Button:
                text: 'Encode'
                on_press: root.encode()
            Button:
                text: "Quit"
                on_press: app.stop()


<FileChooserPopup>:
    title: 'Pick a Color'
    size_hint: 1.0, 0.7
    id: cpopup

    BoxLayout:
        orientation: 'vertical'

        ColorPicker:
            size_hint: 1.0, 1.0

        Button:
            text: 'OK'
            size_hint: 1.0, 0.2
            on_press: root.dismiss()