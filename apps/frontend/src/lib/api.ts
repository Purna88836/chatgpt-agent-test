export async function api<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(process.env.NEXT_PUBLIC_BACKEND_URL + path, options);
  if (!res.ok) throw new Error('API error');
  return res.json() as Promise<T>;
}
