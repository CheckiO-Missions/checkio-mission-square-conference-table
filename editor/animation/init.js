requirejs(['ext_editor_io2', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        function square_conference_table_visualization(tgt_node, data) {
            if (!data || !data.ext) {
                return
            }

            /*
             * edit output value
             */
            try {
                $(tgt_node.parentNode).find(".output").text('Your result:' + list_to_tuple(data.out))
            } catch (e) {
                $(tgt_node.parentNode).find(".output").text('Your result:' + JSON.stringify(data.out))
                return
            }

            /**
             * list_to_tuple (function) 
             */
            function list_to_tuple(ls) {
                let result = '['
                ls.forEach((xs) => {
                    result += '('
                    xs.values.forEach((x) => {
                        result += x + ','
                    })
                    if (xs.values.length > 1) {
                        result = result.slice(0, -1)
                    }
                    result += '), '
                })
                return result.slice(0, -2) + ']'
            }

            /**
             * attr
             */
            const attr = {
                grid: {
                    'stroke-width': '.1px',
                    'stroke': '#82D1F5',
                },
                desk: {
                    'stroke-width': '1px',
                    'stroke': '#333333',
                    'fill': '#82D1F5',
                    'opacity': '0.5',
                },
            }

            /**
             * guard
             */
            if (!data.ext.result) {
                return
            }

            /**
             * values
             */
            const side_length = data.in[1] 
            const output = data.out
            const margin = 10
            const draw_area_edge = 200
            const grid_edge = draw_area_edge / side_length
            const scale = 5 / side_length
            const sum = (ary) => ary.reduce((accumulator, currentValue) => accumulator + currentValue)

            /**
             * paper
             */
            const paper = Raphael(tgt_node, draw_area_edge + margin * 2, draw_area_edge + margin * 2)

            /**
             * draw grid
             */
            for (let y = 0; y <= side_length; y += 1) {
                paper.path(['M', margin, margin + y * grid_edge, 'h', draw_area_edge]).attr(attr.grid).attr(
                    {'stroke-width': scale + 'px'})
            }
            for (let x = 0; x <= side_length; x += 1) {
                paper.path(['M', margin + x * grid_edge, margin, 'v', draw_area_edge]).attr(attr.grid).attr(
                    {'stroke-width': scale + 'px'})
            }

            /**
             * draw desks
             */
            const difs = []
            const desks_dict = {}
            let count = 4
            while (count--) {
                desks = output[count].values
                dif = side_length - sum(desks)
                difs.push(dif)
                if (!(dif in desks_dict)) {
                    desks_dict[dif] = []
                }
                desks_dict[dif].push(desks)
            }
            const tp = difs.sort().join('')
            const tp_dict = {
                '1111': [ [1, 0], [1, 1], [1, 0], [1, 1], ],
                '0112': [ [0, 0], [1, 1], [2, 1], [1, 1], ],
                '0022': [ [0, 0], [2, 1], [2, 1], [0, 0], ],
            }
            const connection_type = tp_dict[tp]

            // draw top desks
            const top_disks = desks_dict[connection_type[0][0]].pop()
            let prev_d = 0
            top_disks.forEach(d => {
                paper.rect(
                    margin + prev_d * grid_edge, margin,
                    d * grid_edge, grid_edge
                ).attr(attr.desk)
                prev_d += d
            })

            // draw left desks
            const left_disks = desks_dict[connection_type[1][0]].pop()
            prev_d = 0
            left_disks.forEach(d => {
                paper.rect(
                    margin, margin + (prev_d + connection_type[1][1]) * grid_edge,
                    grid_edge, grid_edge * d
                ).attr(attr.desk)
                prev_d += d
            })

            // draw right desks
            const right_disks = desks_dict[connection_type[2][0]].pop()
            prev_d = 0
            right_disks.forEach(d => {
                paper.rect(
                    margin + grid_edge * (side_length - 1), margin + (prev_d + tp_dict[tp][2][1]) * grid_edge,
                    grid_edge, grid_edge * d
                ).attr(attr.desk)
                prev_d += d
            })

            // draw bottom desks
            const bottom_disks = desks_dict[connection_type[3][0]].pop()
            prev_d = 0
            bottom_disks.forEach(d => {
                paper.rect(
                    margin + (prev_d + tp_dict[tp][3][1]) * grid_edge, margin + grid_edge * (side_length - 1),
                    d * grid_edge, grid_edge,
                ).attr(attr.desk)
                prev_d += d
            })
        }

        var io = new extIO({
            animation: function ($expl, data) {
                square_conference_table_visualization(
                    $expl[0],
                    data,
                );
            }
        });
        io.start();
    }
);
