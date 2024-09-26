

# TinyTales - AI-Powered Story Generator

TinyTales is an AI-powered micro-SaaS platform that generates engaging audio stories and accompanying video thumbnails based on user-provided text prompts. This project was created for the lablab.ai hackathon using ElevenLabs Voice AI and various other technologies.

## Key Features

- **AI Story Generation**: Automatically create captivating audio stories based on user input.
- **Video Thumbnail Generation**: Generate visually appealing thumbnails to pair with audio stories.
- **Easy-to-Use Interface**: Simple text prompt input to get started.
- **Automation & Integration**: Integrates with various AI services for a seamless user experience.

## Technologies Used

The project leverages the following technologies:

- **ChatGPT**: For generating story scripts based on user prompts.
- **ElevenLabs**: To synthesize high-quality audio stories from the generated script.
- **Lumalabs/Fluxai**: To create custom video thumbnails for the stories.
- **BlazeBucket**: Storage solution for saving generated content (audio & video).
- **Next.js**: Front-end framework for building the user interface.
- **FastAPI**: Back-end framework to handle API requests and manage interactions between services.
- **Docker**: For containerizing the application and ensuring smooth deployment.

## Python FastAPI Backend

The flow of TinyTales is simple yet powerful:

1. **User Input**: The user provides a text prompt via the Next.js UI.
2. **ChatGPT Script Generation**: The prompt is passed to ChatGPT to generate a script or story.
3. **ElevenLabs Audio Story Generation**: ElevenLabs takes the generated script and creates an audio version.
4. **Lumalabs Video Thumbnail Generation**: Simultaneously, a video thumbnail is created using Lumalabs/Fluxai.
5. **Output**: The system returns both a short video thumbnail and an MP3 audio file of the story.

## Flowchart Overview

The following flowchart outlines the core process of TinyTales:

<Image src="assets/tinytales-flowchat.png" alt="TinyTales Flowchart" width={800} height={600} />

- **Start**: The user begins by entering a prompt.
- **ChatGPT**: Generates a script or story from the input prompt.
- **ElevenLabs**: Converts the story into an audio format.
- **Lumalabs**: Generates a video thumbnail for the content.
- **Output**: Both the audio story and thumbnail are provided to the user.

## Next.js Frontend UI

- **Technologies**: The front-end is built using Next.js with Tailwind CSS.
- **Input**: Users provide a text prompt to generate the story.
- **Output**: The UI displays the generated video thumbnail and provides a link to download the MP3 audio file.

<Image src="assets/tinytales-idea.png" alt="TinyTales UI" width={800} height={600} />
<Image src="assets/tiny-tales-ui.png" alt="TinyTales UI" width={800} height={600} />

## Future Enhancements

- **Email Notification Integration**: Sending stories and thumbnails to users via email.
- **More AI Models**: Expanding the platform to support multiple AI models for script and video generation.
- **User Accounts**: Enabling users to save and manage their generated stories.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
