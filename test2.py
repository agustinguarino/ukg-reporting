import requests

poc = {
    "Payroll": "agustinignacio.guarinobonahon@ukg.com",
    "GlobalHR": "nawal.jaiswal@ukg.com",
    "TaxCare": "dahiana.fuentescastro@ukg.com"
}

teams = ["Payroll", "GlobalHR", "TaxCare"]

entities = []

for team in teams:
    team_poc = poc[team]

    team_object = {
        "type": "mention",
        "text": f"<at>{team}</at>",
        "mentioned": {
            "id": f"{team_poc}",
            "name": f"{team}"
        }
    }

    entities.append(team_object)

url = "https://kronos.webhook.office.com/webhookb2/267f9212-3f17-417f-9638-a2c6b6a12350@7b6f35d2-1f98-4e5e-82eb-e78f6ea5a1de/IncomingWebhook/01a871d248bc4484802489ed877d23d9/d54f9814-8eab-47a0-8d1e-ecfc0f3c873f"

payload = {
  "type": "message",
  "attachments": [
    {
      "contentType": "application/vnd.microsoft.card.adaptive",
      "contentUrl": "null",
      "content": {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.0",
        "body": [
          {
            "type": "Container",
            "id": "6db1fabd-68a9-22d1-4cc3-310a26aeea24",
            "padding": "None",
            "items": [
              {
                "type": "ColumnSet",
                "id": "fec48ea4-9b5d-b39f-f2a9-359477619294",
                "columns": [
                  {
                    "type": "Column",
                    "id": "a4f0308f-7c40-b435-25ab-3597a8ece759",
                    "padding": "None",
                    "width": "auto",
                    "items": [
                      {
                        "type": "Image",
                        "id": "b3b1e119-f72f-b468-2497-f620304fdebd",
                        "url": "https://cdn0.iconfinder.com/data/icons/shift-interfaces/32/Error-512.png",
                        "width": "140px",
                        "height": "140px"
                      }
                    ]
                  },
                  {
                    "type": "Column",
                    "id": "11f5001c-a71e-37c5-9d95-df7777c7a00f",
                    "padding": "None",
                    "width": "stretch",
                    "items": [
                      {
                        "type": "TextBlock",
                        "id": "21346c1f-42d5-b395-47ea-070f922fd30b",
                        "text": "P0 Quality Gate",
                        "wrap": "true",
                        "size": "extraLarge",
                        "weight": "bolder",
                        "horizontalAlignment": "center"
                      }
                    ],
                    "verticalContentAlignment": "Center",
                    "style": "default",
                    "separator": "true"
                  }
                ],
                "padding": "None"
              }
            ]
          },
          {
            "type": "TextBlock",
            "id": "d13d5ac4-f71f-e234-b5d1-3d9e702ffba5",
            "text": "______________________________________",
            "wrap": "true"
          },
          {
            "type": "Container",
            "id": "a3a5f034-ca5d-53f9-47ce-c2fb96f8e98c",
            "padding": "None",
            "items": [
              {
                "type": "ColumnSet",
                "id": "c201d96b-78eb-0c06-343b-0450d4376ace",
                "columns": [
                  {
                    "type": "Column",
                    "id": "9ac4cfed-699c-f67c-2c8e-a23347b7d59f",
                    "padding": "Medium",
                    "width": "stretch",
                    "items": [
                      {
                        "type": "FactSet",
                        "id": "94a1e5b5-a3b8-5a4d-4fc9-53d9ff4e2f8b",
                        "facts": [
                          {
                            "title": "Tests executed:",
                            "value": "4122"
                          },
                          {
                            "title": "Tests passed:",
                            "value": "4068 (98.8%)"
                          },
                          {
                            "title": "Tests failed:",
                            "value": "49"
                          }
                        ]
                      }
                    ],
                    "horizontalAlignment": "Center",
                    "verticalContentAlignment": "Center"
                  },
                  {
                    "type": "Column",
                    "id": "0605caf8-3fa1-2be0-f318-5746bc9d1cb3",
                    "padding": "None",
                    "width": "stretch",
                    "items": [
                      {
                        "type": "FactSet",
                        "id": "6a43a29b-5290-48d8-3d96-96016740fe17",
                        "facts": [
                          {
                            "title": "Muted tests:",
                            "value": "5"
                          },
                          {
                            "title": "Ignored tests:",
                            "value": "0"
                          },
                          {
                            "title": "New failed tests:",
                            "value": "17"
                          }
                        ]
                      }
                    ],
                    "horizontalAlignment": "Center",
                    "verticalContentAlignment": "Center"
                  }
                ],
                "padding": "None",
                "horizontalAlignment": "Center",
                "style": "emphasis"
              }
            ],
            "horizontalAlignment": "Center",
            "verticalContentAlignment": "Center"
          },
          {
            "type": "Container",
            "id": "54a8dd7d-c383-c209-f265-b84dbe1a62aa",
            "padding": "None",
            "items": [],
            "spacing": "None"
          },
          {
            "type": "Container",
            "id": "1109b3d8-49cc-e250-9f8d-5c2fd0be2566",
            "padding": "Large",
            "items": [
              {
                "type": "TextBlock",
                "id": "db88063f-f26f-fc73-f922-0220ac8b527c",
                "text": "Teams with failures:",
                "wrap": "true",
                "horizontalAlignment": "Center"
              },
              {
                "type": "TextBlock",
                "id": "7a69c0b9-c15e-0c49-338f-ee8178f239aa",
                "text": "{'GlobalBenenfits': 11, 'TaxCare': 1, 'UPM': 4}",
                "wrap": "true",
                "horizontalAlignment": "Center"
              }
            ],
            "style": "emphasis"
          },
          {
            "type": "Container",
            "id": "28329b90-ca63-5359-2edf-7d37e9513a1f",
            "padding": "None",
            "spacing": "None"
          },
          {
            "type": "Container",
            "id": "7d945a99-1793-8b00-ef93-836b6459ace4",
            "padding": "None",
            "items": [
              {
                "type": "ColumnSet",
                "id": "5f033a72-562f-daaf-438c-5193e5bec308",
                "columns": [
                  {
                    "type": "Column",
                    "id": "4e91bd46-483b-01eb-4b17-d817b5c7f783",
                    "padding": "Medium",
                    "width": "stretch",
                    "items": [
                      {
                        "type": "FactSet",
                        "id": "3d7cbdce-603a-de17-3a66-23a4455224bd",
                        "facts": [
                          {
                            "title": "Queued date:",
                            "value": "2024-01-27 16:00:24"
                          },
                          {
                            "title": "Started date:",
                            "value": "2024-01-27 16:26:40"
                          },
                          {
                            "title": "Finish date:",
                            "value": "2024-01-27 20:22:14"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "Column",
                    "padding": "Medium",
                    "width": "stretch",
                    "items": [
                      {
                        "type": "FactSet",
                        "id": "72c173a4-3be6-f01a-7f91-00152e3ea912",
                        "facts": [
                          {
                            "title": "From queue to finish:",
                            "value": "4:21:50"
                          },
                          {
                            "title": "From start to finish:",
                            "value": "3:55:34"
                          },
                          {
                            "title": "Test execution time:",
                            "value": "1:17:06"
                          }
                        ]
                      }
                    ]
                  }
                ],
                "padding": "None"
              }
            ],
            "style": "emphasis"
          },
          {
            "type": "TextBlock",
            "id": "681ba7b0-ea3e-c621-01cf-3a923a332ba2",
            "text": "______________________________________",
            "wrap": "true"
          },
          {
            "type": "Container",
            "id": "c21cb369-e892-95d4-7e92-b8fb4cd66a42",
            "padding": "None",
            "items": [
              {
                "type": "ColumnSet",
                "id": "0d8b09d3-7566-65c9-f1a7-da26901675f2",
                "columns": [
                  {
                    "type": "Column",
                    "id": "6757c53a-6ec9-1798-415a-96a61bcb53e6",
                    "padding": "None",
                    "width": "auto",
                    "items": [
                      {
                        "type": "Image",
                        "id": "75bb5ec6-9f87-4c39-b763-b5b7538f347a",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Eo_circle_green_checkmark.svg/1200px-Eo_circle_green_checkmark.svg.png",
                        "size": "Medium",
                        "width": "140px",
                        "height": "140px"
                      }
                    ]
                  },
                  {
                    "type": "Column",
                    "padding": "None",
                    "width": "stretch",
                    "items": [
                      {
                        "type": "TextBlock",
                        "id": "f3d468f7-128b-e850-6a1c-d4e7af9431b7",
                        "text": "P1 Quality Gate",
                        "wrap": "true",
                        "size": "ExtraLarge",
                        "weight": "Bolder",
                        "horizontalAlignment": "Center"
                      }
                    ],
                    "horizontalAlignment": "Center",
                    "verticalContentAlignment": "Center"
                  }
                ],
                "padding": "None"
              }
            ]
          },
          {
            "type": "Container",
            "id": "66f9263c-017c-8c34-6e45-b12f9a6a1162",
            "padding": "None",
            "spacing": "None"
          },
          {
            "type": "Container",
            "id": "0f5a0203-66d6-00fa-472d-5e0c03dd92c2",
            "padding": "Medium",
            "items": [
              {
                "type": "TextBlock",
                "id": "f7f53d53-6663-230d-150e-3ce734503779",
                "text": "Work in progress...",
                "wrap": "true",
                "size": "Medium",
                "color": "Accent",
                "weight": "Bolder",
                "horizontalAlignment": "Center"
              }
            ],
            "style": "emphasis"
          },
          {
            "type": "Container",
            "id": "ecd9dfa8-e821-de0c-9bda-92d4e8cebeba",
            "padding": "None",
            "spacing": "None"
          }
        ],
        "padding": "None"
      }
    }
  ]
}

req = requests.post(url=url, json=payload)
print(req.status_code)