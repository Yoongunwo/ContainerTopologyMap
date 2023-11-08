import React, { useRef, useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import * as d3 from 'd3';

import {
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    Typography,
} from '@mui/material';

import theme from '../../styles/theme';
import { fetchNodeList } from '../../services/sshService';
import containerImage from '../../static/images/docker-container.png';
import kubernetesNodeImage from '../../static/images/kubernetes-node.png';

const Topology = () => {
    const navigate = useNavigate();
    const svgRef = useRef(null);
    const [data, setData] = useState({});
    const [nodeList, setNodeList] = useState(null);
    const [tableHeader, setTableHeader] = useState([]);
    const [tableData, setTableData] = useState([]);

    useEffect(() => {
        fetchNodeList().then((response) => {
            if (response.status !== 200) {
                navigate('/');
            }
            const nodes = response.json().then((data) => {
                setData(data);
                console.log(data);
            });
        });
    }, []);

    useEffect(() => {
        const width = window.innerWidth;

        const root = d3.hierarchy(data);
        const dx = 50;
        const dy = width / (root.height + 1);
        const tree = d3.tree().nodeSize([dx, dy]);
        root.sort((a, b) => d3.ascending(a.data.label, b.data.label));
        console.log('root', root);
        console.log('height', root.height);
        console.log('tree', tree);
        tree(root);

        let x0 = Infinity;
        let x1 = -x0;
        root.each((d) => {
            if (d.x > x1) x1 = d.x;
            if (d.x < x0) x0 = d.x;
        });

        const height = x1 - x0 + dx * 2;
        const svg = d3
            .select(svgRef.current)
            .attr('width', width)
            .attr('height', height)
            .attr('viewBox', [-dy / 3, x0 - dx, width, height])
            .attr(
                'style',
                'max-width: 100%; height: auto; font: 10px sans-serif',
            );

        const link = svg
            .append('g')
            .attr('fill', 'none')
            .attr('stroke', '#555')
            .attr('stroke-opacity', 0.4)
            .attr('stroke-width', 1.5)
            .selectAll()
            .data(root.links())
            .join('path')
            .attr(
                'd',
                d3
                    .linkHorizontal()
                    .x((d) => d.y)
                    .y((d) => d.x),
            );
        const node = svg
            .append('g')
            .attr('stroke-linejoin', 'round')
            .attr('stroke-width', 3)
            .selectAll()
            .data(root.descendants())
            .join('g')
            .attr('transform', (d) => `translate(${d.y},${d.x})`);

        node.append('image')
            .attr('xlink:href', (d) => {
                if (d.data.kind == 'node') return kubernetesNodeImage;
                else if (d.data.kind == 'pod') return containerImage;
            }) // 이미지 파일의 경로
            .attr('x', -20) // 이미지 가로 크기 조정
            .attr('y', -20) // 이미지 세로 크기 조정
            .attr('width', 60) // 이미지 가로 크기 조정
            .attr('height', 40); // 이미지 세로 크기 조정

        /*         node.append('circle')
            .attr('fill', (d) => (d.children ? '#555' : '#999'))
            .attr('r', 2.5); */

        node.append('text')
            .attr('dy', '1.5em')
            .attr('x', (d) => (d.children ? -6 : 6))
            .attr('text-anchor', 'middle')
            .style('font-size', '15px')
            .text((d) => d.data.name)
            .clone(true)
            .lower()
            .attr('stroke', 'white');

        node.on('click', (event, d) => {
            console.log('click', d.data);
            const tableHeader = [];
            const tableData = [];
            Object.entries(d.data).forEach(([key, value]) => {
                if (key === 'children' || key === 'kind') return;
                tableHeader.push(key);
                tableData.push(value);
            });
            setTableHeader(tableHeader);
            setTableData(tableData);
            /* setTableData(d); */
        });
        console.log(svg.node());
    }, [data]);

    return (
        <div className="flex w-full flex-col">
            <div className="w-full">
                <svg ref={svgRef}></svg>
            </div>
            <div className="w-full">
                <TableContainer>
                    <Table>
                        <TableHead
                            style={{ background: theme.palette.primary.main }}
                        >
                            <TableRow>
                                {tableHeader.map((data) => (
                                    <TableCell
                                        key={data}
                                        style={{
                                            color: theme.typography.primaryText
                                                .color,
                                        }}
                                    >
                                        {data}
                                    </TableCell>
                                ))}
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            <TableRow>
                                {tableData.map((data) => (
                                    <TableCell key={data}>{data}</TableCell>
                                ))}
                            </TableRow>
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
        </div>
    );
};

export default Topology;
