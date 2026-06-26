export interface PublicPageSummary {
  title: string;
  kind: string;
  path: string;
  tags: string[];
  links: string[];
}

interface PagesResponse {
  pages: PublicPageSummary[];
}

export async function fetchPublicPages(): Promise<PublicPageSummary[]> {
  const response = await fetchWithStaticFallback("/api/pages", `${import.meta.env.BASE_URL}pages/index.json`);

  if (!response.ok) {
    throw new Error(`获取知识花园页面失败：${response.status}`);
  }

  const body = (await response.json()) as PagesResponse;
  return body.pages;
}

async function fetchWithStaticFallback(apiPath: string, staticPath: string): Promise<Response> {
  try {
    const apiResponse = await fetch(apiPath);

    if (apiResponse.ok) {
      return apiResponse;
    }
  } catch {
    // Static deployments do not have the FastAPI backend available.
  }

  return fetch(staticPath);
}
