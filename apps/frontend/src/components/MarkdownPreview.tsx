import ReactMarkdown from 'react-markdown';

export function MarkdownPreview({ content }: { content: string }) {
  return <ReactMarkdown>{content}</ReactMarkdown>;
}
