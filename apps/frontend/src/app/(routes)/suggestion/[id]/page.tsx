interface Props { params: { id: string } }
export default function SuggestionPage({ params }: Props) {
  return <div>Suggestion {params.id}</div>;
}
