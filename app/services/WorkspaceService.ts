import http from '../common/http';
import {
    IProject,
    ICreateProjectArgs
} from '../common/types';

export interface IWorkspaceService {
    get(identifier: string): Promise<IProject>;
    getAll(): Promise<IProject[]>;
    create(args: ICreateProjectArgs): Promise<IProject>;
    delete(identifier: string): Promise<void>;
}

export class WorkspaceService implements IWorkspaceService {
    public async create({ name }: ICreateProjectArgs): Promise<IProject> {
        const response = await http.post<IProject>(
            `/projects/`,
            {
                "name": name,
            }
        );

        return response.data;
    }

    public async get(identifier: string): Promise<IProject> {
        const response = await http.get<IProject>(
            `/projects/${identifier}/`
        );

        return response.data;
    }

    public async delete(identifier: string): Promise<void> {
        await http.delete(`/projects/${identifier}`);
    }

    public async getAll(): Promise<IProject[]> {
        const response = await http.get<IProject[]>(
            `/projects/`
        );

        return response.data;
    }
}
