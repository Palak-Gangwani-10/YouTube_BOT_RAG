from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled


def fetch_transcript(video_id: str, lang: str = "en") -> str:
    """
    Fetch and flatten the transcript of a YouTube video.

    Args:
        video_id (str): The YouTube video ID (not the full URL)
        lang (str): Language code for the transcript (default: "en")

    Returns:
        str: Flattened transcript as a single string

    Raises:
        Exception: If transcript is not available
    """
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
        transcript = " ".join(chunk["text"] for chunk in transcript_list)
        return transcript
    except TranscriptsDisabled:
        raise Exception("Transcripts are disabled or not available for this video.")
