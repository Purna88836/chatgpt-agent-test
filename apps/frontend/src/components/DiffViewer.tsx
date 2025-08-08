import ReactDiffViewer from 'react-diff-viewer';

export function DiffViewer({ oldText, newText }: { oldText: string; newText: string }) {
  return <ReactDiffViewer oldValue={oldText} newValue={newText} />;
}
